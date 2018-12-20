<style>
.myButton {
    -moz-box-shadow:inset 0px -3px 7px 0px #29bbff;
    -webkit-box-shadow:inset 0px -3px 7px 0px #29bbff;
    box-shadow:inset 0px -3px 7px 0px #29bbff;
    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #2dabf9), color-stop(1, #0688fa));
    background:-moz-linear-gradient(top, #2dabf9 5%, #0688fa 100%);
    background:-webkit-linear-gradient(top, #2dabf9 5%, #0688fa 100%);
    background:-o-linear-gradient(top, #2dabf9 5%, #0688fa 100%);
    background:-ms-linear-gradient(top, #2dabf9 5%, #0688fa 100%);
    background:linear-gradient(to bottom, #2dabf9 5%, #0688fa 100%);
    filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#2dabf9', endColorstr='#0688fa',GradientType=0);
    background-color:#2dabf9;
    -moz-border-radius:3px;
    -webkit-border-radius:3px;
    border-radius:3px;
    border:1px solid #0b0e07;
    display:inline-block;
    cursor:pointer;
    color:#ffffff;
    font-family:Arial;
    font-size:15px;
    padding:9px 23px;
    text-decoration:none;
    text-shadow:0px 1px 0px #263666;
}
.myButton:hover {
    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #0688fa), color-stop(1, #2dabf9));
    background:-moz-linear-gradient(top, #0688fa 5%, #2dabf9 100%);
    background:-webkit-linear-gradient(top, #0688fa 5%, #2dabf9 100%);
    background:-o-linear-gradient(top, #0688fa 5%, #2dabf9 100%);
    background:-ms-linear-gradient(top, #0688fa 5%, #2dabf9 100%);
    background:linear-gradient(to bottom, #0688fa 5%, #2dabf9 100%);
    filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#0688fa', endColorstr='#2dabf9',GradientType=0);
    background-color:#0688fa;
}
.myButton:active {
    position:relative;
    top:1px;
}

</style>

<?php
require_once 'users/init.php';
require_once $abs_us_root.$us_url_root.'users/includes/header.php';
require_once $abs_us_root.$us_url_root.'users/includes/navigation.php';
require 'Zebra_Pagination.php';
?>

<?php
if (!securePage($_SERVER['PHP_SELF'])){die();}
?>

<div id="page-wrapper">
    <div class="container-fluid">
        <!-- Page Heading -->
        <h1>
            <?php
            if($user->isLoggedIn()) {
                echo "Welcome ".$user->data()->fname." ".$user->data()->lname;
                echo "<br>";
            }else {
                echo "Welcome Guest";
            }
            ?>
        </h1>
    </div> <!-- /.container -->
    <table class="table table-striped">
        <thead>
            <tr class="row-name">
                <th style="width:15%">ID</th>
                <th>Source</th>
                <th>Folder</th>
                <th>Start time</th>
                <th>End time</th>
                <th>Status</th>
                <th>Report</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $records_per_page = 5;
            $pagination = new Zebra_Pagination();
            $db2 = DB2::getInstance();
            $sql='SELECT * FROM status_table where source='.'"JUDY2_Research"';
            $query_miseqs = $db2->query($sql);
            $count = $query_miseqs->count();
            $sql = 'SELECT * FROM status_table where source='.'"JUDY2_Research"'.' LIMIT ' . (($pagination->get_page() - 1) * $records_per_page) . ', ' . $records_per_page . '';
            $query_miseqs = $db2->query($sql);
            $djresults=$query_miseqs->results();
            //dump($djresults);
            $pagination->records($count);
            $pagination->records_per_page($records_per_page);
            foreach ($djresults as $qq){
            ?>
                <tr class="row-content">
                    <td><?php echo $qq->bccdc_id;?></td>
                    <td><?php echo $qq->source;?></td>
                    <td><?php echo $qq->folder;?></td>
                    <td><?php echo $qq->start_time;?></td>
                    <td><?php echo $qq->end_time;?></td>
                    <td> <?php echo $qq->status;?></td>
                    <td>
                        <?php if($qq->status=="Status_OK") {?>
                            <a href="show.php?name=<?php echo $qq->folder?>&id=<?php echo $qq->bccdc_id?>">
                                <button type="button" class="myButton">Report</button>
                            </a>
                        <?php } ?>
                    </td>
                </tr>
                <?php
                // render the pagination links
                $pagination->render();
                ?>
        </tbody>
    </table>
</div> <!-- /.wrapper -->


<?php
require_once $abs_us_root.$us_url_root.'users/includes/page_footer.php'; // the final html footer copyright row + the external js calls
?>

<!-- Place any per-page javascript here -->

<?php
require_once $abs_us_root.$us_url_root.'users/includes/html_footer.php'; // currently just the closing /body and /html
?>
